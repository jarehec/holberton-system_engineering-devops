#!/usr/bin/env ruby
# regular expression that matches hbtn where 't' can be repeated 2-5 times
puts ARGV[0].scan(/hbt{2,5}n/).join
