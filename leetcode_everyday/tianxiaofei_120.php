<?php

class Solution
{

    function minimumTotal($triangle)
    {
        $i = 0;
        foreach ($triangle as $key => &$val) {
            if ($key == 0) {
                continue;
            } else {
                foreach ($val as $k => &$v) {
                    if ($key == 1) {
                        $v += $triangle[0][0];
                    } else {
                        if(!isset($triangle[$key - 1][$k]))
                        {
                            $v += $triangle[$key - 1][$k - 1];
                        }
                        elseif($k==0)
                        {
                            $v += $triangle[$key - 1][0];
                        }
                        else
                        {
                        if ($triangle[$key - 1][$k] > $triangle[$key - 1][$k - 1]) {
                            $v += $triangle[$key - 1][$k - 1];
                        } else {
                            $v += $triangle[$key - 1][$k];
                        }
                        }
                    }
                }
            }
            $i++;
        }
        $arr = sort($triangle[$i]);
        return $triangle[$i][0];
    }
}
$arr = array(array(2),array(3,4),array(6,5,7),array(4,1,8,3));
$obj = new Solution();
$ret = $obj->minimumTotal($arr);
var_dump($ret);
