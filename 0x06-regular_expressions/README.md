# 0x06. Regular expression


## Background Context

For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the `//`:

```sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```

### 0-simply_match_school.rb
Simply matching `School`<br>
Requirements:
  - The regular expression must match `School`
  - Create a Ruby script that accepts one argument and pass it to a regular expression matching method

### 1-repetition_token_0.rb
Repetition Token #0<br>
Requirements:
  - Find the regular expression that will match the [above cases](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/e7db3c377d46453588fc84f3a975661d142fee91.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231128%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231128T155114Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e9883a4254a8fa7043aa8b472dbf2766c1e2e539532642a9e6b787a16e359673)
  - Create a Ruby script that accepts one argument and pass it to a regular expression matching method
