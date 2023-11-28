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

### 2-repetition_token_1.rb
Repetition Token #1 <br>
Requirements:
  - Find the regular expression that will match the [above cases](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/c59ff11db195d5cf17d1790a5141ae2f234786d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231128%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231128T155114Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d9f43137cd784fefc3bc745d9a54aab7e5c69326ae45c3df64cfe76f197f6858)
  - Create a Ruby script that accepts one argument and pass it to a regular expression matching method

### 3-repetition_token_2.rb
Repetition Token #2 <br>
Requirements:
  - Find the regular expression that will match the [above cases](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/3b6bf4aeca6a0c2de584e7f5d68d11eef57ce205.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231128%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231128T155114Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a0222a54139db93abe0ccf69bb155d8d9fa95c34ee1a0bacd158fbe3035595a8)
  - Create a Ruby script that accepts one argument and pass it to a regular expression matching method

### 4-repetition_token_3.rb
Repetition Token #3 <br>
Requirements:
  - Find the regular expression that will match the [above cases](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/f8dbcb9cf5ae569a8645027dc46e81cb372ce28e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231128%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231128T155114Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3abff02b24fd9aa702eef7e1140bc1e1e159bf359f3aec9089aef07d57d43a37)
  - Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
  - Your regex should not contain square brackets

### 5-beginning_and_end.rb
Not quite HBTN yet <br>
Requirements:
  - The regular expression must be exactly matching a string that starts with `h` ends with `n` and can have any single character in between
  - Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

### 6-phone_number.rb
Call me maybe <br>
This task is brought to you by a professional advisor [Neha Jain](https://intranet.alxswe.com/rltoken/GqwvXAvTXR_JXqyTvZ4AzQ), Senior Software Engineer at LinkedIn <br>
Requirement:
  - The regular expression must match a 10 digit phone number

### 7-OMG_WHY_ARE_YOU_SHOUTING.rb
OMG WHY ARE YOU SHOUTING? <br>
Requirement:
  - The regular expression must be only matching: capital letters
