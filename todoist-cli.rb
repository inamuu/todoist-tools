require 'trollop'

def tasks
  puts "tasksだよ"
end

opts = Trollop::options do
  opt :tasks, 'Display all tasks'
end

Trollop::die "need at least one options" if ARGV.empty?

p opts
p opts[:tasks]

if opts.has_key?[:tasks]
  tasks
end