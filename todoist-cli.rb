require 'trollop'

def tasks
  puts "tasksだよ"
end

opts = Trollop::options do
  opt :tasks, 'タスク一覧を表示する'
end

Trollop::die "need at least one options" unless opts.values.any?

tasks if opts[:tasks] == true
