<?php


class lock
{
    private static $_instance;

    private $zk_obj;

    private static $global_path='/lock';

    private function __construct($ip, $port)
    {
        $this->zk_obj = new Zookeeper($ip . ':' . $port);
    }


    public function get_instance()
    {
        if (!(self::$_instance instanceof self)) {
            self::$_instance = new self();
        }
        return self::$_instance;
    }

    private function create_tmp_node($path)
    {
        $acl = array(
            array(
                'perms' => Zookeeper::PERM_ALL,
                'scheme' => 'world',
                'id' => 'anyone',
            ));
        return $zookeeper->create($path, "1000", $acl, Zookeeper::EPHEMERAL);

    }


    public static function lock()
    {



    }

    public static function release()
    {

    }

}