"""
main
"""
from hello import concat
from hello.hello import VInt, VStr

n = VInt(10)
s = VStr("aaaa")


print(concat.pair(n, s))
