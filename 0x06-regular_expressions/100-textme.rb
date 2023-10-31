#!/usr/bin/env ruby

arg = ARGV[0]
print arg.scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(,)
