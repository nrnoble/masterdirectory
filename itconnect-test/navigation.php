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
 * The websites navigation bar at the top providing the tab for: internship table, student resources,
 *      and official program website.
 */
?>

<link rel='shortcut icon' type='image/x-icon' href='/favicon.ico' />
<nav class="navbar navbar-inverse navbar-fixed-top">
    <div class="container-fluid">
        <div class="navbar-header">
            <!-- Phone pills -->
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar"
                    aria-expanded="false" aria-controls="navbar">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <!-- /Phone pills -->
            <a class="navbar-brand" href="/index.php">
                <img style="max-width:100px; max-height:40px; margin-top: -9px;" alt="Green River"
                     src="/assets/img/grtech.jpg">
            </a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/views/internships.php">Internships</a>
                </li>
                <li>
                    <a href="/views/studentResources.php">
                        Student Resources
                    </a>
                </li>
                <li>
                    <a href="http://www.greenriver.edu/academics/areas-of-study/bas-programs.htm" target="_blank">Earn your Bachelors
                        degree</a>
                </li>
                <li>
                    <a href="/views/newsletter.php" class="highlight">
                        Get Updates
                    </a>
                </li>
            </ul>
            <?php echo $logOutButton; ?>
        </div>
    </div>
</nav>
