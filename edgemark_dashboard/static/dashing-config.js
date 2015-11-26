var dashboard = new Dashboard();
dashboard.addWidget('total_work_completed', 'Number', {
    getData: function () {
        var self = this;
        Dashing.utils.get('total_work_completed', function(data) {
            $.extend(self.data, data);
        });
    },
    interval: 300000
});