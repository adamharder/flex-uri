from flexuri.parsed_uri import ParsedUri
from flexuri.functions import wrap
from python.common.util_res import project_root
from redis import Redis
from pathlib import Path
import pytest
def get_test_res():
    test_res = Path(__file__).absolute().parent/"res"
    assert test_res.is_dir()
    return test_res


def test_bad():
    with pytest.raises(Exception):
        ParsedUri.wrap("")
    with pytest.raises(Exception):
        ParsedUri.wrap("https://x.com??")


"""
def test_file_uri():
    print(get_test_res())
    x = get_test_res()/"sample1_raw.cfs"
    xx=f"file://{x.absolute()}"

    f=flex_uri.FlexURI(xx)
    assert str(f)==f"file://{x.absolute()}"
    assert str(f.parent)==f"file://{x.absolute().parent}"
    assert str(f.suffix)==x.absolute().suffix
    assert not f.is_dir()
    assert f.is_file()
    assert f.read(length=3)==b'CFS'
    assert flex_uri.FlexURI("file:///").parent==flex_uri.FlexURI("file:///")
    assert flex_uri.FlexURI("file:///xx/yy").parent==flex_uri.FlexURI("file:///xx")
    assert flex_uri.FlexURI("file:///xx/yy.txt").stem=="yy"
    assert flex_uri.FlexURI("file:///xx/yy.txt").suffix==".txt"
    assert flex_uri.FlexURI("file:///xx/yy.txt").name=="yy.txt"
    assert flex_uri.FlexURI("file:///").name == ""
    assert flex_uri.FlexURI("file:///xx/yy.txt") == flex_uri.FlexURI("file:///xx/yy.txt")
    assert flex_uri.FlexURI("file:///xx/yy.txt") != flex_uri.FlexURI("file:///xx/yy.tx")
"""

def test_redis_hash_uri():
    print(get_test_res())
    x = get_test_res()/"sample1_raw.cfs"
    xx=f"redis_hash:///xxx/yyy.zzz"
    print(xx)

    from python.flex_uri.util_redis_hash import RedisHashUri
    f=RedisHashUri.wrap(xx)
    import arrow
    hash_name="test_flex_uri"
    field_name="f1"
    Redis().hdel(hash_name, field_name)
    assert Redis().hget(hash_name, field_name) is None

    uri=f"redis_hash:///{hash_name}/{field_name}"
    assert RedisHashUri.wrap(uri=uri).is_dir() == False    
    assert RedisHashUri.wrap(uri=uri).is_file() == False    
    
    
    test_val=str(arrow.now()).encode()
    RedisHashUri.wrap(uri=uri).write(value=test_val)
    assert RedisHashUri.wrap(uri=uri).is_dir() == False    
    assert RedisHashUri.wrap(uri=uri).is_file() == True



    f.write(value=test_val)
    assert test_val==f.read()
    assert RedisHashUri.wrap('redis_hash:///xxx/i_do_not_exist').is_file() == False
    assert RedisHashUri.wrap('redis_hash:///xxx/i_do_not_exist').is_dir() == False
    assert RedisHashUri.wrap('redis_hash:///xxx/i_do_not_exist').read() is None

    
    print(x)
    
    
    # print(f)
    # print(dir(f))
    # assert f.is_dir()==False
    # print(str(f.path))
    # print(str(f.path))
    # print(str(f.stem))
    # print(str(f.suffix))
    
    #assert f.path==Path("/xxx/yyy.zzz")
    # flex_uri.FlexURI(xx)
    # from python.flex_uri import util_redis_hash
    # assert str(f)==f"redis_hash:///xxx/yyy.zzz"
    # assert str(f.parent)==f"redis_hash:///xxx/yyy.zzz"
    # assert str(f.suffix)==".zzz"
    # assert not f.is_dir()
    # assert f.is_file()
    # assert f.read(length=3)==b'CFS'
    # assert flex_uri.FlexURI("redis_hash:///").parent==flex_uri.FlexURI("redis_hash:///")
    # assert flex_uri.FlexURI("redis_hash:///xx/yy").parent==flex_uri.FlexURI("redis_hash:///xx")
    # assert flex_uri.FlexURI("redis_hash:///xx/yy.txt").stem=="yy"
    # assert flex_uri.FlexURI("redis_hash:///xx/yy.txt").suffix==".txt"
    # assert flex_uri.FlexURI("redis_hash:///xx/yy.txt").name=="yy.txt"
    # assert flex_uri.FlexURI("redis_hash:///").name == ""
    # assert flex_uri.FlexURI("redis_hash:///xx/yy.txt") == flex_uri.FlexURI("redis_hash:///xx/yy.txt")
    # assert flex_uri.FlexURI("redis_hash:///xx/yy.txt") != flex_uri.FlexURI("redis_hash:///xx/yy.tx")

