<template>
  <div>
    <div class="small">
  <b-table hover :fields="columns" :items="tableData"></b-table>
</div>
<div class="small">         <!-- <line-chart></line-chart> -->
 <canvas ref="canvas" width="900" height="400" />
</div>
  </div>
</template>
    
<script>
import axios from 'axios';
// import Vuetable from 'vuetable-2'
// import { Line } from 'vue-chartjs'
import { Line } from 'vue-chartjs'
  
export default {
    extends: Line,
  components: {
    // Vuetable,
    Line
  },
  name: 'Dashboard',
  data() {
    return {
      msg: '',
      chartdata: {
      labels: ['January', 'February'],
      datasets: [
        {
          label: 'Data One',
          backgroundColor: '#f87979',
          data: [40, 20]
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false
    },
      columns: [ {
            key: 'stateOrUnionTerritory',
            sortable: true
          },{
            key: 'confirmedIndianNational',
            sortable: true
          }, {
            key: 'confirmedForeignNational',
            sortable: true
          }, {
            key: 'cured',
            sortable: true
          },
          {
            key: 'deaths',
            sortable: true
          }],
        tableData: []
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/get-statecount';
      axios.get(path)
        .then((res) => {
          this.tableData = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },
  mounted() {
    this.getMessage();
    this.renderChart({
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
      datasets: [
        {
          label: 'GitHub Commits',
          backgroundColor: '#f87979',
          data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 11]
        }
      ]
    })
  },
};
</script>
<style>
  .small {
    max-width: 600px;
    margin:  150px auto;
  }
</style>
