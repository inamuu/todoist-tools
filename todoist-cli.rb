require 'trollop'
require 'dotenv'
require 'net/http'
require 'uri'

Dotenv.load

def tasks
  uri = URI.parse(ENV["apiurl"])
  request = Net::HTTP::Post.new(uri)
  request.set_form_data(
    "resource_types" => "[\"projects\"]",
    "token" => ENV["apitoken"]
  )

  req_options = {
    use_ssl: uri.scheme == "https",
  }

  response = Net::HTTP.start(uri.hostname, uri.port, req_options) do | http |
    http.request(request)
  end
  puts response.body
end

opts = Trollop::options do
  opt :tasks, 'タスク一覧を表示する'
end

Trollop::die "need at least one options" unless opts.values.any?

tasks if opts[:tasks] == true
