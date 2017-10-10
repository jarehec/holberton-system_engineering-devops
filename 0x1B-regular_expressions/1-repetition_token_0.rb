#!/usr/bin/env ruby
# regular expression that matches hbtn where 't' can be repeated
puts ARGV[0].scan(/hbt*n/).join
