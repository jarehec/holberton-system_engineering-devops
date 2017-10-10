#!/usr/bin/env ruby
# regular expression that matches hbtn where 't' is repeated once or more
puts ARGV[0].scan(/hbt+n/).join
