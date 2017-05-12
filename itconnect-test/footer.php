<?php
/**
MIT License

Copyright (c) 2016 Michael Lant, Bogdan Pshonyak, Yegor Shemereko

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
 */

/**
 * The footer of the whole website providing links to social media, official GRC website and Admin-Login page
 */
?>

<!-- Footer seperated for code re-use -->
<footer class="footer">

    <!--Brand Logo -->
    <div class="row col-md-3 col-sm-12 text-center fblock">
        <a href="http://www.greenriver.edu/bas" target="_blank">
            <h1 class="created-by-text">
                Made with <i class="fa fa-heart" aria-hidden="true"></i> by <br> Green River College students
            </h1>
        </a>
    </div>

    <div class="row col-md-3 col-sm-12 text-center fblock">
        <strong>Main Campus:</strong><br>
        <p class="text-center"><a class="footer-link" target="_blank"
                                  href="https://www.google.com/maps/place/Green+River+Community+College/@47.3130745,-122.179769,16z/data=!4m2!3m1!1s0x549058a045230aab:0x296322357297393b">
          <span class="medium-font">12401 Southeast 320th Street<br>
          Auburn, WA 98092</span>
            </a></p>
        <strong>Kent Station Campus:</strong>
        <br>
        <p class="text-center"><a target="_blank"
                                  class="footer-link" href="https://www.google.com/maps/place/Green+River+Community+College-Kent+Campus/@47.3840959,-122.2356563,17z/data=!4m6!1m3!3m2!1s0x54905bfe4208b423:0xcf6efc0630023899!2sGreen+River+Community+College-Kent+Campus!3m1!1s0x54905bfe4208b423:0xcf6efc0630023899">
          <span class="medium-font">417 Ramsay Way #112<br>
          Kent, WA 98032</span>
            </a></p>
    </div>

    <!-- Social Media Buttons and Icons -->
    <div class="row col-md-3 col-sm-12 text-center fblock">
        <strong>Follow us on:</strong>
        <div class="Social-Media">
            <a class="icons" href="https://www.facebook.com/greenrivertechnologyprograms" target="_blank">
                <i class="fa fa-facebook-square" aria-hidden="true"></i>
            </a>
            <a class="icons" href="http://instagram.com/greenrivertech" target="_blank">
                <i class="fa fa-instagram" aria-hidden="true"></i>
            </a>
            <a class="icons" href="https://www.linkedin.com/groups?home=&gid=6781985&trk=anet_ug_hm" target="_blank">
                <i class="fa fa-linkedin-square" aria-hidden="true"></i>
            </a>
        </div>
    </div>

    <!-- Other Links -->
    <div class="row col-md-3 col-sm-12 text-center fblock">
        <strong>Earn Your Bachelor's Degree in:</strong>
        <div class="Social-Media2">
            <p class="">
                <a class="footer-link"
                   href="http://www.greenriver.edu/academics/areas-of-study/bas-programs/software-development.htm?utm_source=baslanding&utm_medium=banner&utm_content=baslink&utm_campaign=bassoftwaredev">Software
                    Development</a>
            </p>

            <p class="">
                <a class="footer-link"
                   href="http://www.greenriver.edu/academics/areas-of-study/bas-programs/network-administration-and-security.htm?utm_source=baslanding&utm_medium=banner&utm_content=baslink&utm_campaign=basnetworking">Network
                    Administration & Security</a>
            </p>

            <p class="admin-link-wrapper">
                <a class="admin-link" href="/views/adminLogin.php">Admin Login</a>
            </p>
        </div>
    </div>
</footer>
