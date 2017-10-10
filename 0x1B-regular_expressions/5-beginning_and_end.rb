#!/usr/bin/env ruby
# regular expression that matches a string that starts with 'h' and ends with 'n' and can have any single character in between
puts ARGV[0].scan(/h.n/).join
