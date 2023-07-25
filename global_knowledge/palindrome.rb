puts "Word ?"
word = gets.chomp.downcase

# Fast
# puts word == word.reverse ? ">>> Palindrome" : ">>> Nope"

# Manual
word.chars.each_with_index do | letter, index_from_start |
	index_from_end = word.size - 1 - index_from_start
	break if (index_from_start > index_from_end)
	if (word[index_from_start] != word[index_from_end])
		puts ">>> Nope" 
		exit
	end
end
puts ">>> Palindrome !"

