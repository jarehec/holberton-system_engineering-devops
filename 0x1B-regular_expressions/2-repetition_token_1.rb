#!/usr/bin/env ruby
# regular expression that matches hbtn where 't' is optional
puts ARGV[0].scan(/hbt{0,1}n/).join
