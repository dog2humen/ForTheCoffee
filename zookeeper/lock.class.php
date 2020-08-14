<?php


class lock
{
    private static $_instance;

    private static $zk_obj;

    private static $global_lock_path='/lock';
    private static $znode = '';
	private static $isNotifyed;

    private function __construct($ip, $port)
    {
        self::$zk_obj = new Zookeeper($ip . ':' . $port);
		$is_global_node = self::$zk_obj->exists(self::$global_lock_path);
		if($is_global_node===false)
		{
			self::create_node(self::$global_lock_path);
		}
    }


    public function get_instance($ip,$port)
    {
        if (!(self::$_instance instanceof self)) {
            self::$_instance = new self($ip,$port);
        }
        return self::$_instance;
    }
	
	private static function create_node($path)
    {
        $acl = array(
            array(
                'perms' => Zookeeper::PERM_ALL,
                'scheme' => 'world',
                'id' => 'anyone',
            ));
        return self::$zk_obj->create($path, "1000", $acl);

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

    public static function watcher(){
		self::$isNotifyed = true;
        return self::lock();
    }

	public static function lock(){
		if(empty(self::$znode))
		{
			$node_path = self::create_tmp_node(self::$global_lock_path."/n");
			self::$znode = str_replace(self::$global_lock_path."/","",$node_path);
		}
		return self::get_lock();
	}

	private static function is_pre()
	{
		$childrens = self::$zk_obj->getchildren(self::$global_lock_path);
        if(!empty($childrens))
        {
            sort($childrens);
            if($childrens[0] == self::$znode)
            {
                return true;
            }
		}
		return $childrens[0];
	}

    public static function get_lock()
    {
		$is_pre = self::is_pre();
		if($is_pre === true)
		{
			return true;
		}
		else
		{
			self::$isNotifyed = false;
			$result = self::$zk_obj->get(self::$global_lock_path."/".$is_pre, [lock::class, 'watcher']);
			while(!$result)
			{
				$res = self::is_pre();
				if($res === true)
				{
					return true;
				}
				else
				{
					$result = self::$zk_obj-->get(self::$global_lock_path."/".$is_pre, [lock::class, 'watcher']);
				}
			}
			while(!self::$isNotifyed)
			{
				echo '.';
				sleep(1);
			}
			return true;
		}
		return true;
    }
    public static function release()
    {
        return self::$zk_obj->delete(self::$znode);
    }

}
$lock = lock::get_instance('127.0.0.1','2181');
$have_lock = $lock::lock();
var_dump($have_lock);
if($have_lock === true)
{
	sleep(20);

}
