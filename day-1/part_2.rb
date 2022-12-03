INPUT_FILE = "input_1.txt"

def solve()
    elves = Array.new
    current_calories = 0
    f = File.open(INPUT_FILE, "r") do |f|
        f.each { |line|
            line.chomp!
            if line == ""
                elves << current_calories 
                current_calories = 0
            else
                current_calories += Integer(line)
            end
        }
    end
    elves.sort!
    elves.reverse!
    puts elves[0] + elves[1] + elves[2]
end

solve