module.exports = {
    proxy: {
        '/apis':{
            traget:'http://127.0.0.1:5000',
            changeOrigin:true,
            pathRewite:{
                '^/apis':''
            }
        }
    }
}