#!/usr/bin/env ruby
txt = ARGV[0].scan(/\[from:(.*?)\]|\[to:(.*?)\]|\[flags:(.*?)\]/).join(" ")
txt = txt.squeeze(' ')
l = txt.split
puts l.join(',')
