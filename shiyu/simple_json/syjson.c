#include <assert.h> /* assert() */
#include <errno.h>  /* errno, ERANGE */
#include <stdlib.h> /* NULL, malloc(), realloc(), free(), strtod() */
#include <math.h>   /* HUGE_VAL */
#include <string.h> /* memcpy() */
#include <stdio.h> /* sprintf() printf() */

#include "syjson.h"



//默认栈大小
#ifndef SYJSON_PARSE_STACK_INIT_SIZE
#define SYJSON_PARSE_STACK_INIT_SIZE 256

#endif

//默认字符串化栈大小
#ifndef SYJSON_PARSE_STRINGIFY_INIT_SIZE
#define SYJSON_PARSE_STRINGIFY_INIT_SIZE 256

#endif

//解析数字判断
#define ISDIGIT(string) ((string) >= '0' && (string) <= '9')
#define ISDIGIT1TO9(string) ((string) >= '1' && (string) <= '9')
//解析字符串错误
#define STRING_ERROR(ret) do{ c->top = head; return ret; }while(0)
//字符校验断言
#define EXPECT(c, ch)  do{ assert(*c->json == (ch)); c->json++; }while(0)
//压栈操作，单个字符写入到新地址
#define PUTC(c, ch) do{ *(char*)syjson_content_push(c, sizeof(char)) = (ch); }while(0)
//字符串内存复制
#define PUTS(c, s, len) memcpy(syjson_content_push(c, len), s, len)

//过滤空白
static void syjson_parse_whitespace(syjson_content* c)
{
    const char* p = c->json;
    while(*p == ' ' || *p == '\t' || *p == '\n' || *p == '\r')
        p++;
    c->json = p;
}
//解析完毕尾部字符判断
static int syjson_parse_root_not_singular(syjson_content* c, syjson_value* v)
{
    syjson_parse_whitespace(c);
    if(*c->json == '\0')
        return SYJSON_PARSE_OK;
    else
    {
        v->type = SYJSON_NULL;
        return SYJSON_PARSE_ROOT_NOT_SINGULAR;
    }
}
//多类型入栈
static void* syjson_content_push(syjson_content* c, size_t size)
{
    void* ret;
    assert(size > 0);
    //检查是否超出栈空间
    if(c->top + size >= c->size)
    {
        //初始化栈空间
        if(c->size == 0)
            c->size = SYJSON_PARSE_STACK_INIT_SIZE;
        //一点五倍增量增加栈空间回退至初次分配地址的可能，减少内存碎片
        while(c->top + size >= c->size)
            c->size += c->size >> 1;
        //申请堆内存，制作栈空间
        c->stack = (char*) realloc(c->stack, c->size);
    }
    ret = c->stack + c->top;
    c->top += size;
    //返回栈顶地址
    return ret;
}
//弹出指定栈数据
static void* syjson_content_pop(syjson_content* c, size_t len)
{
    assert(c->top >= len);
    //根据栈顶和长度返回当前出栈地址
    return c->stack + (c->top -= len);
}
//释放栈空间
void syjson_free(syjson_value* v)
{
    assert(v != NULL);
    size_t i;
    switch(v->type)
    {
        case SYJSON_STR:
            free(v->val.str.s);
            break;
        case SYJSON_ARR:
            for (i = 0; i < v->val.arr.s; i++)
            {
                //释放数组内元素
                syjson_free(&v->val.arr.e[i]);
            }
            //释放数组内元素
            free(v->val.arr.e);
            break;
        case SYJSON_OBJ:
            for(i = 0;i < v->val.obj.s; i++)
            {
                //释放对象内成员key
                free(v->val.obj.m[i].k);
                //释放对象内成员
                syjson_free(&v->val.obj.m[i].v);
            }
            free(v->val.obj.m);
            break;
        default:
            break;
    }
    v->type = SYJSON_NULL;
}
//解析null类型
static int syjson_parse_null(syjson_content* c, syjson_value* v)
{
    EXPECT(c, 'n');
    if(c->json[0] != 'u' || c->json[1] != 'l' || c->json[2] != 'l')
        return SYJSON_PARSE_INVALID_VALUE;
    c->json += 3;
    v->type = SYJSON_NULL;
    return SYJSON_PARSE_OK;
}
//解析FALSE类型
static int syjson_parse_false(syjson_content* c, syjson_value* v)
{
    EXPECT(c, 'f');
    if(c->json[0] != 'a' || c->json[1] != 'l' || c->json[2] != 's' || c->json[3] != 'e')
        return SYJSON_PARSE_INVALID_VALUE;
    c->json += 4;
    v->type = SYJSON_FALSE;
    return SYJSON_PARSE_OK;
}
//解析TRUE类型
static int syjson_parse_true(syjson_content* c, syjson_value* v)
{
    EXPECT(c, 't');
    if(c->json[0] != 'r' || c->json[1] != 'u' || c->json[2] != 'e')
        return SYJSON_PARSE_INVALID_VALUE;
    c->json += 3;
    v->type = SYJSON_FALSE;
    return SYJSON_PARSE_OK;
}
//重构三种字面量类型解析
static int syjson_parse_literal(syjson_content* c, syjson_value* v, const char* literal, syjson_type type)
{
    size_t i;
    EXPECT(c, literal[0]);
    for(i = 0; literal[i + 1]; i++)
        if(c->json[i] != literal[i + 1])
            return SYJSON_PARSE_INVALID_VALUE;
    c->json += i;
    v->type = type;
    return SYJSON_PARSE_OK;
}
//json字符串字面量转换double
static int syjson_parse_number(syjson_content* c, syjson_value* v)
{
    const char* p = c->json;
    //负号
    if(*p == '-') p++;
    //整数
    if(*p == '0') p++;
    else
    {
        if(!ISDIGIT1TO9(*p)) return SYJSON_PARSE_INVALID_VALUE;
        for(p++; ISDIGIT(*p); p++);
    }
    //小数
    if(*p == '.')
    {
        p++;
        if(!ISDIGIT(*p)) return SYJSON_PARSE_INVALID_VALUE;
        for(p++; ISDIGIT(*p); p++);
    }
    //指数
    if(*p == 'e' || *p == 'E')
    {
        p++;
        if(*p == '-' || *p == '+') p++;
        if(!ISDIGIT(*p)) return SYJSON_PARSE_INVALID_VALUE;
        for(p++; ISDIGIT(*p); p++);
    }

    //函数校验数字真实性
    v->val.num = strtod(c->json, NULL);
    if(errno = ERANGE && (v->val.num == HUGE_VAL || v->val.num == -HUGE_VAL))
        return SYJSON_PARSE_NUMBER_TOO_BIG;
    c->json = p;
    v->type = SYJSON_NUM;
    return SYJSON_PARSE_OK;
}
//解析JSON转码至UNICODE码点，int4字节存储
static const char* syjson_parse_hex4(const char* p, unsigned* u)
{
    int i;
    *u = 0;
    //UNICODE基本面码点
    for(i = 0;i < 4;i++)
    {
        char ch = *p++;
        //16进制对应4位二进制
        *u <<= 4;
        //按位或写入数据，区分大小写
        if      (ch >= '0' && ch <= '9') *u |= ch - '0';
        //16进制，加上前缀十进制
        else if (ch >= 'A' && ch <= 'F') *u |= ch - ('A' - 10);
        else if (ch >= 'a' && ch <= 'f') *u |= ch - ('a' - 10);
        else return NULL;
    }
    return p;
}
//UNICODE转至UTF-8编码格式
static void syjson_encode_utf8(syjson_content* c, unsigned u)
{
    //unicode码点，右移位数请查阅UTF-8编码实现
    if(u <= 0x007f)
        PUTC(c, u & 0xff);
    else if(u <= 0x07ff)
    {
        PUTC(c, ((u >> 6) & 0x1f) | 0xc0);
        PUTC(c, ( u       & 0x3f) | 0x80);
    }
    else if(u <= 0xffff)
    {
        PUTC(c, ((u >> 12) & 0x0f) | 0xe0);
        PUTC(c, ((u >>  6) & 0x3f) | 0x80);
        PUTC(c, ( u        & 0x3f) | 0x80);
    }
    else if(u <= 0x10ffff)
    {
        PUTC(c, ((u >> 18) & 0x08) | 0xf0);
        PUTC(c, ((u >> 12) & 0x3f) | 0x80);
        PUTC(c, ((u >> 6)  & 0x3f) | 0x80);
        PUTC(c, ( u        & 0x3f) | 0x80);
    }
}
//写入字符串到值
static int syjson_string_to_value(syjson_content* c, char** str, size_t* len)
{
    size_t head = c->top;
    unsigned u, u2;
    const char* p;
    //检查字符串初始字符，并向后位移指针
    EXPECT(c, '\"');
    p = c->json;
    for(;;)
    {
        char ch = *p++;
        switch(ch)
        {
            //解析字符串结束，获取字符串长度，批量写入字符空间
            case '\"':
                *len = c->top - head;
                *str = syjson_content_pop(c, *len);
                c->json = p;
                return SYJSON_PARSE_OK;
            //解析转义
            case '\\':
                switch(*p++)
                {
                    //转义字符压栈
                    case '\"': PUTC(c, '\"'); break;
                    case '\\': PUTC(c, '\\'); break;
                    case '/' : PUTC(c, '/' ); break;
                    case 'b' : PUTC(c, '\b'); break;
                    case 'f' : PUTC(c, '\f'); break;
                    case 'n' : PUTC(c, '\n'); break;
                    case 'r' : PUTC(c, '\r'); break;
                    case 't' : PUTC(c, '\t'); break;
                    //解析UTF-8
                    case 'u':
                        //验证进制合法，并前移字符指针
                        if(!(p = syjson_parse_hex4(p, &u)))
                            STRING_ERROR(SYJSON_PARSE_INVALID_UNICODE_HEX);
                        //高代理码点
                        if(u >= 0xd800 && u <= 0xdbff)
                        {
                            if(*p++ != '\\')
                                STRING_ERROR(SYJSON_PARSE_INVALID_UNICODE_SURROGATE);
                            if(*p++ != 'u')
                                STRING_ERROR(SYJSON_PARSE_INVALID_UNICODE_SURROGATE);
                            if(!(p = syjson_parse_hex4(p, &u2)))
                                STRING_ERROR(SYJSON_PARSE_INVALID_UNICODE_HEX);
                            //低代理码点
                            if(u2 < 0xdc00 || u2 > 0xdfff)
                                STRING_ERROR(SYJSON_PARSE_INVALID_UNICODE_SURROGATE);
                            //辅助平面码点合并，0x10000 至 0x10ffff，总共20bit数据，高位10bit，低位10bit
                            u =  0x10000 + (((u - 0xd800) << 10) | (u2 - 0xdc00));
                        }
                        //编码为UTF-8，并压栈
                        syjson_encode_utf8(c, u);
                    break;
                    default:
                        STRING_ERROR(SYJSON_PARSE_INVALID_STRING_ESCAPE);
                }
                break;
            case '\0':
                STRING_ERROR(SYJSON_PARSE_MISS_QUOTATION_MARK);
            default:
                //忽略控制字符和需转义字符
                if((unsigned char)ch < 0x20 || (unsigned char)ch == 0x7F)
                    STRING_ERROR(SYJSON_PARSE_INVALID_STRING_CHAR);
                //压入单个字符
                PUTC(c, ch);
        }
    }
}
//解析字符串
static int syjson_parse_string(syjson_content* c, syjson_value* v)
{
    int ret;
    char* s;
    size_t len;
    ret = syjson_string_to_value(c, &s, &len);
    if(ret == SYJSON_PARSE_OK)
    {
        syjson_set_string(v, s, len);
    }
    return ret;
}
//向前声明处理依赖
static int syjson_parse_value(syjson_content* c, syjson_value* v);
//解析数组
static int syjson_parse_array(syjson_content* c, syjson_value* v)
{
    size_t i, size = 0;
    int ret;
    EXPECT(c, '[');
    //过滤空数组
    syjson_parse_whitespace(c);
    if(*c->json == ']')
    {
        c->json++;
        v->type = SYJSON_ARR;
        v->val.arr.s = 0;
        v->val.arr.e = NULL;
        return SYJSON_PARSE_OK;
    }
    for(;;)
    {
        syjson_value e;
        syjson_init(&e);
        ret = syjson_parse_value(c, &e);
        if(ret != SYJSON_PARSE_OK)
            break;
        memcpy(syjson_content_push(c, sizeof(syjson_value)), &e, sizeof(syjson_value));
        size++;
        syjson_parse_whitespace(c);
        if(*c->json == ',')
        {
            c->json++;
            syjson_parse_whitespace(c);
        }
        else if(*c->json == ']')
        {
            c->json++;
            v->type = SYJSON_ARR;
            v->val.arr.s = size;
            size *= sizeof(syjson_value);
            memcpy(v->val.arr.e = (syjson_value*)malloc(size), syjson_content_pop(c, size), size);
            //解析成功 直接返回
            return SYJSON_PARSE_OK;
        }
        else
        {
            ret = SYJSON_PARSE_MISS_COMMA_OR_SQUARE_BRACKET;
            break;
        }
    }
    //释放空间弹出的栈帧空间
    for (i = 0; i < size; i++)
        syjson_free((syjson_value*)syjson_content_pop(c, sizeof(syjson_value)));

    return ret;
}
//解析对象
static int syjson_parse_object(syjson_content* c, syjson_value* v)
{
    size_t i, size;
    syjson_member m;
    int ret;
    EXPECT(c, '{');
    syjson_parse_whitespace(c);
    //空对象
    if(*c->json == '}')
    {
        c->json++;
        v->type = SYJSON_OBJ;
        v->val.obj.m = 0;
        v->val.obj.s = 0;
        return SYJSON_PARSE_OK;
    }
    m.k = NULL;
    size = 0;
    for (;;)
    {
        char* str;
        syjson_init(&m.v);

        if(*c->json != '"')
        {
            ret = SYJSON_PARSE_MISS_KEY;
            break;
        }
        //解析对象键
        ret = syjson_string_to_value(c, &str, &m.kl);
        if(ret != SYJSON_PARSE_OK)
            break;
        memcpy(m.k = (char*)malloc(m.kl + 1), str, m.kl);
        m.k[m.kl] = '\0';
        syjson_parse_whitespace(c);
        //判断键值对分隔符
        if(*c->json != ':')
        {
            ret = SYJSON_PARSE_MISS_COLON;
            break;
        }
        c->json++;
        syjson_parse_whitespace(c);
        //解析对象值
        ret = syjson_parse_value(c, &m.v);
        if(ret != SYJSON_PARSE_OK)
            break;
        memcpy(syjson_content_push(c, sizeof(syjson_member)), &m, sizeof(syjson_member));
        size++;
        m.k = NULL;
        syjson_parse_whitespace(c);
        if(*c->json == ',')
        {
            c->json++;
            syjson_parse_whitespace(c);
        }
        else if(c->json[0] == '}')
        {

            //对象解析完毕
            c->json++;
            size_t size_all = sizeof(syjson_member) * size;
            v->type = SYJSON_OBJ;
            v->val.obj.s = size;
            memcpy(v->val.obj.m = (syjson_member*)malloc(size_all), syjson_content_pop(c, size_all), size_all);
            return SYJSON_PARSE_OK;
        }
        else
        {
            ret = SYJSON_PARSE_MISS_COMMA_OR_CURLY_BRACKET;
            break;
        }
    }
    //解析失败释放解析对象成员占用的堆内存空间
    free(m.k);
    for(i = 0; i < size; i++)
    {
        syjson_member* m = (syjson_member*)syjson_content_pop(c, sizeof(syjson_member));
        free(m->k);
        syjson_free(&m->v);
    }
    v->type = SYJSON_NULL;

    return ret;
}

//解析json入口
static int syjson_parse_value(syjson_content* c, syjson_value* v)
{
    switch(*c->json)
    {
        case 'n' : return syjson_parse_literal(c, v, "null", SYJSON_NULL);break;
        case 'f' : return syjson_parse_literal(c, v, "false", SYJSON_FALSE);break;
        case 't' : return syjson_parse_literal(c, v, "true", SYJSON_TRUE);break;
        case '"' : return syjson_parse_string(c, v);break;
        case '[' : return syjson_parse_array(c, v);break;
        case '{' : return syjson_parse_object(c, v);break;
        case '\0': return SYJSON_PARSE_EXPECT_VALUE;break;
        default  : return syjson_parse_number(c, v);break;
    }
}

//json库入口
int syjson_parse(syjson_value* v, const char* json)
{
    syjson_content c;
    int ret;
    assert(v != NULL);
    c.json = json;
    c.stack = NULL;
    c.size = c.top = 0;
    syjson_init(v);
    syjson_parse_whitespace(&c);
    ret = syjson_parse_value(&c, v);

    if(SYJSON_PARSE_OK == ret)
        ret = syjson_parse_root_not_singular(&c, v);

    assert(c.top == 0);
    free(c.stack);

    return ret;
}

//逆向字符串生成UTF-8码点
static void syjson_stringify_string(syjson_content* c, const char* s, size_t len) {
    assert(s != NULL);
    size_t i, size;
    char* head, *p;
    static const char hex_digits[] = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F' };

    //根据转义\u00xx结构预分配最大栈空间
    p = head = syjson_content_push(c, size = len * 6 + 2);
    *p++ = '"';
    for (i = 0; i < len; i++) {
        unsigned char ch = (unsigned char)s[i];
        switch (ch) {
            case '\"': *p++ = '\\'; *p++ = '\"'; break;
            case '\\': *p++ = '\\'; *p++ = '\\'; break;
            case '\b': *p++ = '\\'; *p++ = 'b';  break;
            case '\f': *p++ = '\\'; *p++ = 'f';  break;
            case '\n': *p++ = '\\'; *p++ = 'n';  break;
            case '\r': *p++ = '\\'; *p++ = 'r';  break;
            case '\t': *p++ = '\\'; *p++ = 't';  break;
            default:
                //处理需转移字符后，其他二进制不转义
                if (ch < 0x20 || ch == 0x7F)
                {
                    *p++ = '\\'; *p++ = 'u'; *p++ = '0'; *p++ = '0';
                    *p++ = hex_digits[ch >> 4];
                    *p++ = hex_digits[ch & 15];
                }
                else
                {
                    *p++ = s[i];
                }
        }
    }
    *p++ = '"';
    //缩减的分配最大栈空间，但缩减出的栈空间并未释放，等待弹出栈释放
    c->top -= size - (p - head);
}
//逆向json结构
static void syjson_stringify_value(syjson_content* c, const syjson_value* v) {
    size_t i;
    switch (v->type) {
        case SYJSON_NULL:   PUTS(c, "null",  4); break;
        case SYJSON_FALSE:  PUTS(c, "false", 5); break;
        case SYJSON_TRUE:   PUTS(c, "true",  4); break;
        case SYJSON_NUM: c->top -= 32 - sprintf(syjson_content_push(c, 32), "%.17g", v->val.num); break;
        case SYJSON_STR: syjson_stringify_string(c, v->val.str.s, v->val.str.l); break;
        case SYJSON_ARR:
            PUTC(c, '[');
            for (i = 0; i < v->val.arr.s; i++) {
                if (i > 0)
                    PUTC(c, ',');
                syjson_stringify_value(c, &v->val.arr.e[i]);
            }
            PUTC(c, ']');
            break;
        case SYJSON_OBJ:
            PUTC(c, '{');
            for (i = 0; i < v->val.obj.s; i++) {
                if (i > 0)
                    PUTC(c, ',');
                syjson_stringify_string(c, v->val.obj.m[i].k, v->val.obj.m[i].kl);
                PUTC(c, ':');
                syjson_stringify_value(c, &v->val.obj.m[i].v);
            }
            PUTC(c, '}');
            break;
        default: assert(0 && "invalid type");
    }
}
//结构逆向字符串化入口
char* syjson_stringify(const syjson_value* v, size_t* length) {
    syjson_content c;
    assert(v != NULL);

    c.stack = (char*)malloc(c.size = SYJSON_PARSE_STRINGIFY_INIT_SIZE);
    c.top = 0;
    syjson_stringify_value(&c, v);

    if (length) *length = c.top;

    PUTC(&c, '\0');

    return c.stack;
}


//写入布尔值
void syjson_set_boolean(syjson_value* v, int boolean)
{
    assert(v != NULL);
    syjson_free(v);
    v->type = boolean ? SYJSON_TRUE : SYJSON_FALSE;
}
//写入数字
void syjson_set_number(syjson_value* v, double num)
{
    assert(v != NULL);
    syjson_free(v);
    v->type = SYJSON_NUM;
    v->val.num = num;
}
//从字符串栈写入值空间
void syjson_set_string(syjson_value* v, const char* s, size_t len)
{
    assert(v != NULL && (s != NULL || len == 0));
    syjson_free(v);
    v->val.str.s = (char*)malloc(len + 1);
    memcpy(v->val.str.s, s, len);
    v->val.str.s[len] = '\0';
    v->val.str.l = len;
    v->type = SYJSON_STR;
}

//返回json数据类型
syjson_type syjson_get_type(const syjson_value* v)
{
    assert(v != NULL);
    return v->type;
}
//返回真假值，并非变量类型
int syjson_get_boolean(const syjson_value* v)
{
    assert(v != NULL && (v->type == SYJSON_TRUE || v->type == SYJSON_FALSE));
    return v->type == SYJSON_TRUE;
}
//返回数字类型
double syjson_get_number(const syjson_value* v)
{
    assert(v != NULL && v->type == SYJSON_NUM);
    return v->val.num;
}
//返回字符串长度
size_t syjson_get_string_length(const syjson_value* v)
{
    assert(v != NULL && v->type == SYJSON_STR);
    return v->val.str.l;
}
//返回字符串
const char* syjson_get_string(const syjson_value* v)
{
    assert(v != NULL && v->type == SYJSON_STR);
    return v->val.str.s;
}
//获取数组大小
size_t syjson_get_array_size(const syjson_value* v)
{
    assert(v != NULL && v->type == SYJSON_ARR);
    return v->val.arr.s;
}
//获取数组元素
syjson_value* syjson_get_array_element(const syjson_value* v, size_t index)
{
    assert(v != NULL && v->type == SYJSON_ARR);
    //指针越界
    assert(index <= v->val.arr.s);
    return &v->val.arr.e[index];
}
//获取对象数量
size_t syjson_get_object_size(const syjson_value* v)
{
    assert(v != NULL && v->type == SYJSON_OBJ);
    return v->val.obj.s;
}
//获取对象键
const char* syjson_get_object_key(const syjson_value* v, size_t index)
{
    assert(v != NULL && v->type == SYJSON_OBJ);
    //成员越界
    assert(index < v->val.obj.s);
    return v->val.obj.m[index].k;
}
//获取对象键，字符串长度
size_t syjson_get_object_key_length(const syjson_value* v, size_t index)
{
    assert(v != NULL && v->type == SYJSON_OBJ);
    assert(index < v->val.obj.s);
    return v->val.obj.m[index].kl;
}
//获取对象值
syjson_value* syjson_get_object_value(const syjson_value* v, size_t index)
{
    assert(v != NULL && v->type == SYJSON_OBJ);
    assert(index < v->val.obj.s);
    return &v->val.obj.m[index].v;
}
