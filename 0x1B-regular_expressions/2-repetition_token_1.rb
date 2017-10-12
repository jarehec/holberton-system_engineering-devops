#!/usr/bin/env ruby
# regular expression that matches hbtn where 'b' is optional
puts ARGV[0].scan(/hb?tn/).join
