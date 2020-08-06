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


    public function get_instance($ip,$port)
    {
        if (!(self::$_instance instanceof self)) {
            self::$_instance = new self($ip,$port);
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
        return self::$zk_obj->create($path, "1000", $acl, Zookeeper::EPHEMERAL|Zookeeper::SEQUENCE);

    }

    private static function watcher(){
        return self::lock();
    }

    public static function lock(){
        if(empty(self::$znode)){
                self::$znode = self::create_tmp_node(self::$global_path);
            }
        return self::get_lock();
    }


    public static function get_lock()
    {
        $childrens = self::$zk_obj->getchildren('/');
		var_dump($childrens);
        //$childrens = self::$zk_obj->getchildren(self::$global_path);
        if(!empty($childrens))
        {
            sort($childrens);
			var_dump(self::$znode);
            if($childrens[0] == self::$znode)
            {
                return true;
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
$lock = lock::get_instance('127.0.0.1','2181');
$have_lock = $lock::lock();
var_dump($have_lock);die;
