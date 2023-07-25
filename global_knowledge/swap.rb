puts("Number A ?")
a = gets.chomp.to_i
puts "Number B ?"
b = gets.chomp.to_i

puts
puts "A = #{a}, B = #{b}"

puts ">>> SWAP"

a, b = b, a

puts "A = #{a}, B = #{b}"