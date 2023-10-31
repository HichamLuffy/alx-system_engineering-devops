#!/usr/bin/env ruby

arg = ARGV[0]
print arg.scan(/^\d{10}$/).join
