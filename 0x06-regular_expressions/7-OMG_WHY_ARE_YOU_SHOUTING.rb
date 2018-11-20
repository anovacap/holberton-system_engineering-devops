#!/usr/bin/env ruby
txt = ARGV[0].scan(/\[from:(.*?)\]|\[to:(.*?)\]|\[flags:(.*?)\]/)
txt.split(:)
txt.squeeze(' ')
txt.join(,)