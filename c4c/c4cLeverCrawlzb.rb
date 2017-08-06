# zackburt [12:46 PM] 
# Here’s some info on how our internal API works…

# I don’t know if you speak ruby, but hopefully this code-sample is self-documenting.. this is what we call via the ruby crons:

def post_job(title, website, description, utc_datetime, lat = nil, lng = nil, country = nil, employment_type = nil, remote_ok = nil, time_commitment = nil)
    if old_job_listing?(utc_datetime)
        return
    end

   if low_quality_keywords_present?(title, description)
        puts “LQ keywords”
        return
    end

   encoding_options = {
      :invalid           => :replace,  # Replace invalid byte sequences
      :undef             => :replace,  # Replace anything not defined in ASCII
      :replace           => ‘’,        # Use a blank for those replacements
      :universal_newline => true       # Always break lines with \n
    }
    title = title.encode(Encoding.find(‘ASCII’), encoding_options)
    description = description.encode(Encoding.find(‘ASCII’), encoding_options)
    website = website.encode(Encoding.find(‘ASCII’), encoding_options)


   options = {
      :body => {
           :key => @api_key,
           :title => title,
           :website => website,
           :description => description,
           :utc_datetime => utc_datetime,
           :lat => lat,
           :lng => lng,
           :country => country,
           :employment_type => employment_type,
           :remote_ok => remote_ok,
           :time_commitment => time_commitment
      }
   }

  begin
        HTTParty.post(@api_base_url + ‘/api/metum/create’, options)
    rescue Exception => e
        puts e
    end
end

# utc_datetime is utc_datetime.  lat, lng are decimals.  country is a string… for employment_type, remote_ok, time_commitment…

validates :employment_type, :inclusion=> { :in => [‘fte’, ‘contract’, ‘internship’, ‘either’, ‘doesnt_say’] }, :allow_nil => true
validates :remote_ok, :inclusion=> { :in => [‘remote_not_ok’, ‘remote_ok’, ‘doesnt_say’] }, :allow_nil => true
validates :time_commitment, :inclusion=> { :in => [‘fulltime’, ‘parttime’, ‘project’] }, :allow_nil => true

# Internally, we store records as a GigOpportunityMetum object.  These are unique based on website.


# `old_job_listing?` and `low_quality_keywords_present?` are methods that we should just move directly into the API
