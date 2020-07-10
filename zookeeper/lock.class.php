<?php


class lock
{
    private static $_instance;

    private static $zk_obj;

    private static $global_path='/lock';
    private static $znode = '';

    private function __construct($ip, $port)
    {
        self::$zk_obj = new Zookeeper($ip . ':' . $port);
    }


    public function get_instance()
    {
        if (!(self::$_instance instanceof self)) {
            self::$_instance = new self();
        }
        return self::$_instance;
    }

    private static function create_tmp_node($path)
    {
        $acl = array(
            array(
                'perms' => Zookeeper::PERM_ALL,
                'scheme' => 'world',
                'id' => 'anyone',
            ));
        return $zookeeper->create($path, "1000", $acl, Zookeeper::EPHEMERAL|ZOO_SEQUENCE);

    }

    private static function watcher(){
        return self::lock()
    }

    public static function lock(){
        if(empty(self::$znode)){
                self::$znode = self::create_tmp_node(self::$global_path);
            }
        return self::get_lock()
    }


    public static function get_lock()
    {


        $childrens = self::$zk_obj->getchildren(self::$global_path));
        if(!empty($childrens)
        {
            sort($childrens);
            if($childrens[0] == self::$znode)
            {
                reutrn true;
            }
        }
        else
        {
            $result = self::$zk_obj->get(self::$global_path,self::watcher);
        }
        return false;

    }


    public static function release()
    {
        return self::$zk_obj->delete(self::$znode);
    }

}