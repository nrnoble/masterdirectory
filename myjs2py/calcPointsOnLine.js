    // var A = [10, 5];
    // var B = [15, 90];

    var A = [10, 5];
    var B = [15, 90];


    function slope(a, b)
    {
        if (a[0] == b[0])
        {
            return null;
        }

        return (b[1] - a[1]) / (b[0] - a[0]);
    }

    function intercept(point, slope)
    {
        if (slope === null)
        {
            // vertical line
            return point[0];
        }

        return point[1] - slope * point[0];
    }

    var m = slope(A, B);
    var b = intercept(A, m);

    var coordinates = [];
    for (var x = A[0]; x <= B[0]; x++)
    {
        var y = m * x + b;
        //document.write(x + ", " + y +"<br>");
        coordinates.push([x, y]);
    }