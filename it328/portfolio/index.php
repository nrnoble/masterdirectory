<?php include "nrn_head.php";?>

<body class="no-trans">

<?php include "nrn_login_dialog.php" ?>


<?php include "nrn_menubar.php" ?>

<div class="page-wrapper" >


	<!-- main-container start -->
	<!-- ================ -->

	<!-- carousels -->
	<section class="main-container kfb_background">

		<div class="container">
			<div class="row">
				<div class="main col-md-9">

					<div id = "about_neal" class="pageblock">
						<div id="header-3">


							<h2 class="space-top">Neal Noble</h2>
							<div class="separator-2"></div>

							<!-- <img class="img-responsive img-border img-left" src="img/intro-pic.jpg" alt="">  -->
							<hr class="visible-xs">

							<img src="neal_noble_75.png" alt="Neal Noble">


						</div>
					</div>




					<div id = "my_background" class="pageblock">
						<div id="header-45">
							<h2 class="space-top">Background</h2>
							<div class="separator-2"></div>

							<!-- <img class="img-responsive img-border img-left" src="img/intro-pic.jpg" alt="">  -->
							<hr class="visible-xs">

							<p>12 years of testing for Microsoft. Shipping SMS 2.0, BackOffice 4.5, Exchange SDK,
								Exchange 2000 OWA, Exchange 2003 OWA. Responsible for testing high profile features
								and pushing for quality in all test areas. Independently developed automation tools to
								eliminate redundant manual tasks and testing. Over 5 years working outside of Microsoft
								with corporate customers solving desktop software\hardware\networking problems. A
								passion for software and the software development process. </p>

						</div>
					</div>




				<?php include "modal.php" ?>


				<div id =  "contact" class="pageblock" style="display:none ">
					<div id="header-9">
						<h2 class="space-top">Contact</h2>
						<div class="separator-2"></div>
						<a href="nrn.php">Contact</a>
					</div>
				</div>


					<script>
						$("#myModal").draggable({
							handle: ".modal-header"
						});

					</script>

				<!-- main end -->

			</div>

									<!-- sidebar start -->
			<!-- ================ -->

			<!-- sidebar end -->


		</div>
</div>

	</section>
	<!-- main-container end -->

</div>
<!-- page-wrapper end -->

<!-- </div> -->


</body>
</html>