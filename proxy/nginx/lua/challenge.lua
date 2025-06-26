local ck = require "resty.cookie"
local cookie, err = ck:new()
local token = cookie:get("claire_token")

if not token then
    ngx.header["Set-Cookie"] = "claire_token=ok; Path=/; HttpOnly"
    ngx.say("<html><script>location.reload()</script></html>")
    return ngx.exit(ngx.HTTP_OK)
end
