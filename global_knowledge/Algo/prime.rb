require 'prime'

value = ARGV[0].to_i
is_prime = Prime.prime?(value)
puts is_prime ? ">>> Premier" : ">>> Non-premier"