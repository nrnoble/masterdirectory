<?php if (!isset($_SESSION)) {
    session_start();
} ?>
<!DOCTYPE html>
<head>
    <title>ros-bot test</title>

    <!-- Bootstrap core CSS -->
    <link href="../bootstrap/css/bootstrap.css" rel="stylesheet">

    <!-- Bootstrap core CSS -->
<!--    <link href="/../bootstrap/css/bootstrap.css" rel="stylesheet">-->
    <link rel="stylesheet" href="https://code.jquery.com/ui/1.11.1/themes/smoothness/jquery-ui.css"/>
    <link rel="stylesheet" type="text/css" href="//cdn.datatables.net/1.10.11/css/jquery.dataTables.css">

    <script src="https://code.jquery.com/jquery-2.2.2.js"></script>
    <script src="../jquery/jquery-2.2.2.js"></script>
    <script src="../bootstrap/js/bootstrap.min.js"></script>

    <!-- Plugins -->

    <style>
        .hidden
        {
            display: none;
        }

    </style>


</head>
<body>
<h1  onclick="$(BotParameters).toggle();">BotParameters</h1>

<div id="BotParameters" style="display: none">

    [BotParameters]
    BigGuysDetectionDistance = 10<br>
    BigGuysDetectionLifeLimit = 90<br>
    EliteDetectionDistance = 5<br>
    EliteDetectionLifeLimit = 90<br>
    MonsterDetectionDistance = 5<br>
    MonsterDetectionLifeLimit = 50<br>
    ArcaneDectectionDistance = 26<br>
    ArcaneDetectionLifeLimit = 100<br>
    CreepMobArmDectectionDistance = 13<br>
    CreepMobArmDetectionLifeLimit = 90<br>
    PlagueDectectionDistance = 12<br>
    PlagueDetectionLifeLimit = 90<br>
    FrozenPulseDetectionDistance = 15<br>
    FrozenPulseDetectionLifeLimit = 100<br>
    MoltenExplosionDistanceAvoid = 25<br>
    MoltenExplosionDetectionLifeLimit = 100<br>
    MortarDistanceAvoid = 18<br>
    MortarDetectionLifeLimit = 90<br>
    OrbiterDetectionDistance = 15<br>
    OrbiterDetectionLifeLimit = 90<br>
    ThunderstormDetectionDistance = 30<br>
    ThunderstormDetectionLifeLimit = 90<br>
    FrozenDetectionDistance = 21<br>
    FrozenDetectionLifeLimit = 100<br>
    DesecratorDetectionDistance = 8<br>
    DesecratorDetectionLifeLimit = 90<br>
    MagdhaFireFliesDistance = 10<br>
    MagdhaFireFliesDetectionLifeLimit = 100<br>
    GhomGasCloudDetectionDistance = 15<br>
    GhomGasCloudDetectionLifeLimit = 100<br>
    DiabloRingFireDetectionDistance = 10<br>
    DiabloRingFireDetectionLifeLimit = 100<br>
    DiabloBonePrisonDetectionDistance = 10<br>
    DiabloBonePrisonDetectionLifeLimit = 100<br>
    DiabloExpandingFireDetectionDistance = 10<br>
    DiabloExpandingFireDetectionLifeLimit = 100<br>
    ZoltunKulleTwisterDetectionDistance = 10<br>
    ZoltunKulleTwisterDetectionLifeLimit = 100<br>
    ZoltunKulleBubbleDetectionDistance = 15<br>
    ZoltunKulleBubbleDetectionLifeLimit = 100<br>
    ZoltunKulleFallingRocksDetectionDistance = 15<br>
    ZoltunKulleFallingRocksDetectionLifeLimit = 100<br>
    RG10YCirclesDetectionDistance = 13<br>
    RG10YCirclesDetectionLifeLimit = 100<br>
    RG20YCirclesDetectionDistance = 23<br>
    RG20YCirclesDetectionLifeLimit = 100<br>
    Algorithm = StayInFight<br>
    SafeZoneMaxSearchRadius = 70<br>
    AvoidanceMovetimeout = 500<br>
    SafeZoneSearchRadiusDelta = 5<br>
    MorluMeteorDistanceAvoid = 25<br>
    MorluMeteorDetectionLifeLimit = 90<br>
    EmberMeteorsDetectionDistance = 20<br>
    EmberMeteorsDetectionLifeLimit = 90<br>
    DeactivateUnderConduit = False<br>
    DeactivateUnderShield = True<br>
    CorpulentsLifeLimit = 100<br>
    CorpulentsDetectionDistance = 15<br>
    AvoidAffixes = True<br>
    AvoidMonster = True<br>
</div>




</body>
</html>