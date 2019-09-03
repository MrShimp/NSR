<template>
  <div class="table_container">
    <div class="table100-head" style="color:#f78230">
      <table>
        <thead>
          <tr class="row100 head">
            <th class="column1">Name</th>
            <th class="column2">Min</th>
            <th class="column2">Max</th>
            <th class="column3">Description</th>
            <th class="column4">Source</th>
            <th class="column5">Category</th>
          </tr>
        </thead>
      </table>
    </div>
    <div class="table100-body js-pscroll">
      <table>
        <tbody>
          <tr class="row100 body" v-for = "item in items">
            <td class="column1">{{item.Goal}}</td>
            <td class="column2">{{item.Min}}</td>
            <td class="column2">{{item.Max}}</td>
            <td class="column3">{{item.Definition}}</td>
            <td class="column4">{{item.Source}}</td>
            <td class="column5">{{item.Category}}</td>
          </tr>
        </tbody>
      </table>
    </div>
    </div>

  </div>
</template>

<style scoped>
  .table_container{
    width:100%;
    height: 100%;
  }

  .table100 .ps__rail-y {
    width: 9px;
    background-color: transparent;
    opacity: 1 !important;
    right: 5px;
  }

  .table100 .ps__rail-y::before {
    content: "";
    display: block;
    position: absolute;
    background-color: #ebebeb;
    border-radius: 5px;
    width: 100%;
    height: calc(100% - 30px);
    left: 0;
    top: 15px;
  }

  .table100 .ps__rail-y .ps__thumb-y {
    width: 100%;
    right: 0;
    background-color: transparent;
    opacity: 1 !important;
  }

  .table100 .ps__rail-y .ps__thumb-y::before {
    content: "";
    display: block;
    position: absolute;
    background-color: #cccccc;
    border-radius: 5px;
    width: 100%;
    height: calc(100% - 30px);
    left: 0;
    top: 15px;
  }

  [ Table ]*/

  .limiter {
    width: 1366px;
    margin: 0 auto;
  }

  .container-table100 {
    width: 100%;
    min-height: 100vh;
    background: #fff;

    display: -webkit-box;
    display: -webkit-flex;
    display: -moz-box;
    display: -ms-flexbox;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    padding: 33px 30px;
  }

  .wrap-table100 {
    width: 1170px;
  }

  /*//////////////////////////////////////////////////////////////////
  [ Table ]*/
  .table100 {
    background-color: #fff;
  }

  table {
    width: 100%;
  }

  th, td {
    font-weight: unset;
    padding-right: 10px;
  }

  .column1 {
    width: 13%;
    padding-left: 40px;
  }

  .column2 {
    width: 5%;
  }

  .column3 {
    width: 35%;
  }

  .column4 {
    width: 10%;
  }

  .column5 {
    width: 10%;
  }

  .table100-head th {
    padding-top: 18px;
    padding-bottom: 18px;
  }

  .table100-body td {
    padding-top: 16px;
    padding-bottom: 16px;
  }

  /*==================================================================
  [ Fix header ]*/
  .table100 {
    position: relative;
    padding-top: 60px;
  }

  .table100-head {
    width: 100%;
    top: 0;
    left: 0;
  }

  .table100-body {
    max-height: 585px;
    overflow: auto;
  }

  /*==================================================================
  [ Ver2 ]*/

  .table100.ver2 .table100-head {
    box-shadow: 0 5px 20px 0px rgba(0, 0, 0, 0.1);
    -moz-box-shadow: 0 5px 20px 0px rgba(0, 0, 0, 0.1);
    -webkit-box-shadow: 0 5px 20px 0px rgba(0, 0, 0, 0.1);
    -o-box-shadow: 0 5px 20px 0px rgba(0, 0, 0, 0.1);
    -ms-box-shadow: 0 5px 20px 0px rgba(0, 0, 0, 0.1);
  }

  .table100.ver2 th {
    font-family: Lato-Bold;
    font-size: 18px;
    color: #fa4251;
    line-height: 1.4;

    background-color: transparent;
  }

  .table100.ver2 td {
    font-family: Lato-Regular;
    font-size: 15px;
    color: #808080;
    line-height: 1.4;
  }

  .table100.ver2 .table100-body tr {
    border-bottom: 1px solid #f2f2f2;
  }

  /*---------------------------------------------*/

  .table100.ver2 {
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 0px 40px 0px rgba(0, 0, 0, 0.15);
    -moz-box-shadow: 0 0px 40px 0px rgba(0, 0, 0, 0.15);
    -webkit-box-shadow: 0 0px 40px 0px rgba(0, 0, 0, 0.15);
    -o-box-shadow: 0 0px 40px 0px rgba(0, 0, 0, 0.15);
    -ms-box-shadow: 0 0px 40px 0px rgba(0, 0, 0, 0.15);
  }

  .table100.ver2 .ps__rail-y {
    right: 5px;
  }

  .table100.ver2 .ps__rail-y::before {
    background-color: #ebebeb;
  }

  .table100.ver2 .ps__rail-y .ps__thumb-y::before {
    background-color: #cccccc;
  }


</style>

<script>
import routes from '@/router/index'
export default {
  data: function () {
    return {
      items: null
    }
  },
  created: function () {
    this.getTabledata()
  },
  methods: {
    getTabledata: function () {
      var vm = this
      this.$axios.get('static/data/table_about.json' ).then(function (response) {
        vm.items = response.data
        console.log(vm.items)
      })
    },
  }
}
</script>
