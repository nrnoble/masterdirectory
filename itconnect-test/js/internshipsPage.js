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
 * This file holds all the javascript written for the internships page
 */

var $table = $('#internshipsTable');

/**
 * The apply button in the Bootsrap table
 * @param value
 * @param row
 * @param index
 * @returns {string}
 */
function operateFormatter(value, row, index) {
    return [
        '<a class="apply" href="javascript:void(0)" title="Apply">',
        '<i class="glyphicon glyphicon-plus edit-icon"></i>',
        '</a>  '
    ].join('');
}

/**
 * Bootsrap Table configurations
 */
$table.bootstrapTable({
    url: '/api/posts.php',
    pagination: true,
    striped: true,
    search: true,
    columns: [
        {
            field: 'title',
            title: 'Title',
            sortable: true
        }, {
            field: 'company',
            title: 'Company',
            sortable: true
        }, {
            field: 'category',
            title: 'Category',
            sortable: true
        }, {
            field: 'location',
            title: 'Location',
            sortable: true
        },{
            field: 'post_date',
            title: 'Date Posted',
            sortable: true
        }, {
            field: 'operate',
            title: 'Apply Now!',
            align: 'center',
            valign: "middle",
            formatter: operateFormatter
        }
    ],
    onClickCell: function (field, value, row, $element) {

        if(field === "operate") {
            window.open(row.url);
            return;
        }

        $("#postModal").modal("show");

        //Populate from inputs with row data
        $("#title").text(row.title);
        $("#company").text(row.company);
        $("#location").text(row.location);
        $("#hours").text(row.hours);
        $("#description").html(row.description);
        $("#qualifications").html(row.qualifications);
        $("#apply_link").attr("href", row.url || "mailto:" + row.email);

    }
});
