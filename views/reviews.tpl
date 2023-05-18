% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<h3>{{ message }}</h3>
<h4> Write a review </h4>
<form action="/reviews" method='post'>
    <p><textarea  rows="2" cols="50" name="Review" placeholder="Review"></textarea></p>
    <p><input type="text" size="50" name="Username" placeholder="Your login"></p>
    <p><input type="text" size="50" name="Phone" placeholder="Your phone number"></p>
    <p>Phone must be written in +Y-(YYY)-YYY-YY-YY format</p>
    <p><input type="submit" value="Send" class="btn btn-default". ></p>
</form>
<p>Help us by providing feedback</p>
<h5 align="center">Other reviews</h5>
%with open('reviews.txt', 'r') as file:
%    for line in file:
%        userreviews+=line
%        userreviews+='\n'
%end
<p align="center"><textarea rows="10" cols="80">{{ userreviews }}</textarea></p>