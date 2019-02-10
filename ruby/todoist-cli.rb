require 'trollop'
require 'dotenv'
require 'net/http'
require 'uri'
require 'json'

Dotenv.load

def projects
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

  hash = JSON.parse(response.body,  symbolize_names: true)
  hash[:projects].map { | hash | puts hash[:name] }
end

def items
  uri = URI.parse(ENV["apiurl"])
  request = Net::HTTP::Post.new(uri)
  request.set_form_data(
    "resource_types" => "[\"items\"]",
    "token" => ENV["apitoken"]
  )

  req_options = {
    use_ssl: uri.scheme == "https",
  }

  response = Net::HTTP.start(uri.hostname, uri.port, req_options) do | http |
    http.request(request)
  end

  hash = JSON.parse(response.body,  symbolize_names: true)
  hash[:items].map { | hash | puts hash[:content] }
end

opts = Trollop::options do
  opt :projects, 'プロジェクト一覧を表示する'
  opt :items, 'タスク一覧を表示する'
end

Trollop::die "オプションを指定してください" unless opts.values.any?
projects if opts[:projects] == true
items if opts[:items] == true
