<template>
  <div class="index-wrap">
    <div class="index-left">
        <div class="index-left-block">
            <h2>全部产品</h2>
            <template v-for="product in productList">
                <h3 :key="product.id">{{ product.title }}</h3>
                <ul :key="product.id">
                    <li v-for="item in product.list" :key="item.id">
                        <a :href="item.url">{{ item.name }}</a>
                        <span v-if="item.hot" class="hot-tag">HOT</span>
                    </li>
                </ul>
                <div v-if="!product.last" class="hr" :key="product.id"></div>
            </template>
        </div>
        <div class="index-left-block lastest-news">
            <h2>最新消息</h2>
            <ul>
            <li v-for="item in newList" :key="item.id">
                <a :href="item.url" class="new-item">{{item.title}}</a>
            </li>
            </ul>
        </div>

    </div>
    <div class="index-right">
        <div class="index-board-list">
            <div class="index-board-item" v-for="(item, index) in boardList" :key="item.id" :class="[{'line-last' : index % 2 !==0},'index-board-' + index ]">
                <div class="index-board-item-inner">
                    <h2>{{item.title}}</h2>
                    <p>{{item.description}}</p>
                    <div class="index-board-button">
                        <a href="" class="button">立即购买</a>
                    </div>
                </div>                
            </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  data (){
      return {
          boardList:{},
          newList:{},
          productList:{}
      }
    },
  mounted (){
      // 请求本地的数据
      this.getRemotelData()
    },
  methods:{
      getRemotelData(){
        // 使用axios
        return this.axios.get('/apis/data2', {
        // return this.axios.get('apis/data', {
            params: {
                ID: 12345
            }
            })
            .then((response) => {
            console.log(response.data);
            const res = response.data;
            if(res){
                this.productList = res.productList;
                this.newList = res.newList;
                this.boardList = res.boardList;
                console.log(this.productList);
                }
            })
            .catch((error) => {
                console.log(error);
                alert('请求数据失败!');
            });
        }
    }
}
</script>

<style scoped>
.index-wrap {
    width: 1200px;
    margin: 0 auto;
    overflow: hidden;
}
.index-left {
    float: left;
    width: 300px;
    text-align: left;
}
.index-right {
    float: left;
    width: 900px;
}
.index-left-block {
    margin: 15px;
    background: #ffffff;
    box-shadow: 0 0 1px #dddddd;
}
.index-left-block .hr {
    margin-bottom: 20px;
}
.index-left-block h2 {
    background: #4fc08d;
    color: #ffffff;
    padding: 10px 15px;
    margin-bottom: 20px;
}
.index-left-block h3 {
    padding: 0 15px 5px 15px;
    font-weight: bold;
    color: #222222;
}
.index-left-block ul {
    padding: 10px 15px;
}
.index-left-block li {
    padding: 5px;
}
.index-board-list {
    overflow: hidden;
}
.index-board-item {
    float: left;
    width: 400px;
    background: #ffffff;
    box-shadow: 0 0 1px #dddddd;
    padding: 20px;
    margin-right: 20px;
    margin-bottom: 20px;
}
.index-board-item-inner {
    min-height: 125px;
    padding-left: 120px;
}
.index-board-0 .index-board-item-inner{
    background: url(../assets/images/1.png) no-repeat;
}
.index-board-1 .index-board-item-inner{
    background: url(../assets/images/2.png) no-repeat;
}
.index-board-2 .index-board-item-inner{
    background: url(../assets/images/3.png) no-repeat;
}
.index-board-3 .index-board-item-inner{
    background: url(../assets/images/4.png) no-repeat;
}
.index-board-item h2 {
    font-size: 18px;
    font-weight: bold;
    color: #000000;
    margin-bottom: 15px;
}
.line-last {
    margin-right: 0;
}
.index-board-button {
    margin-top: 20px;
}
.lastest-news {
    min-height: 512px;
}
.hot-tag {
    background: red;
    color: #ffffff;
}
.new-item {
    display: inline-block;
    width: 230px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
</style>
