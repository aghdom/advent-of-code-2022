INPUT_FILE = "input_1.txt"

def solve()
    max_calories = 0
    current_calories = 0
    f = File.open(INPUT_FILE, "r") do |f|
        f.each { |line|
            line.chomp!
            if line == ""
                if current_calories >= max_calories
                    max_calories = current_calories
                end
                current_calories = 0
            else
                current_calories += Integer(line)
            end
        }    
    end
    puts max_calories
end

solve