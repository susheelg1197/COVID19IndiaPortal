<template>
<div id="maps-print-sample">
   <div class="col-lg-9 control-section">
        <div class="content-wrapper">
<ejs-maps height="550px" width="100%" ref="maps" id='container' :titleSettings='titleSettings'  :tooltipRender='tooltipRender' format='n' :useGroupingSeparator='useGroupingSeparator' :legendSettings='legendSettings'>
    <e-layers>
        <e-layer :shapeData='shapeData' :shapePropertyPath='shapePropertyPath' :shapeDataPath='shapeDataPath' :dataSource='dataSource' :shapeSettings='shapeSettings' :tooltipSettings='tooltipSettings'></e-layer>
    </e-layers>
</ejs-maps>    

            <div style="float: right; margin-right: 10px;">
             </div>
        </div>
    </div>

    <div class="col-lg-3 property-section">
        <table id="property" title="Properties" style="width: 100%">    
            <tbody><tr id="button-control" style="height: 50px">
                <td align="center">
                    <div>
                <!-- <ejs-button id='togglebtn' :style='style' :cssClass='cssClass' :iconCss='iconCss' :isPrimary='isPrimary' :content='content' isToggle="true" v-on:click.native='clickToggle'></ejs-button> -->
                    </div>
                </td>
            </tr>
        </tbody></table>
    </div>
</div>
</template>
<style>

    #maps-print-sample #button-control {
        width: 100%;
        text-align: center;
    }
    
    #maps-print-sample #control-container {
        padding: 0px !important;
    }
    
    #maps-print-sample .e-play-icon::before {
        content: "\e34b";
    }
</style>
<script>
import axios from 'axios';
import Vue from 'vue';
import { MapsPlugin, Legend, MapsTooltip, MapAjax } from '@syncfusion/ej2-vue-maps';
import { worldMap } from './world-map.js';
import { southAmericaCountryCapitals } from './capitals.js';
// import { ButtonPlugin } from '@syncfusion/ej2-vue-buttons';
Vue.use(MapsPlugin);
export default Vue.extend({
  data:function(){
      return{
        statecount:[],
        useGroupingSeparator: true,
        titleSettings: {
            text: 'State-wise India Covid-19 Count',
            textStyle: {
                size: '16px'
            },
        },
        legendSettings: {
            visible: true,
            mode: 'Interactive',
            position: 'Bottom',
            height: '10',
            width: '350',
            labelDisplayMode: 'Trim',
            alignment: 'Center'
        },
        shapeData: worldMap,
        shapeDataPath: 'name',
        shapePropertyPath: 'name',
        dataSource: [{ "name": "Maharashtra", "confirmedIndianNational": 37252895, "color": "#004374" }],
        shapeSettings: {
            border: {
                width: 0.5,
                color: 'gray'
                },
        colorValuePath: 'confirmedIndianNational',
        colorMapping: [
                        {
                            from: 0, to: 100, color: '#dae8f1', label: '<100'
                        },
                        {
                            from: 100, to: 200, color: '#b0cde1', label: '100-200'
                        },
                        {
                            from: 200, to: 400, color: '#90bad8', label: '200-400'
                        },
                        {
                            from: 400, to: 600, color: '#6ea7d2', label: '400-600'
                        },
                        {
                            from: 600, to: 700, color: '#4c96cb', label: '600-700'
                        },
                        {
                            from: 700, to: 1000, color: '#3182bd', label: '700-1k'
                        },
                        {
                            from: 1000, to: 100000, color: '#004374', label: '>1000'
                        }
                    ]
            },
        tooltipSettings: {
                    visible: true,
                    valuePath: 'confirmedIndianNational',
                    format: 'State: ${name} <br> Confirmed Patients: ${confirmedIndianNational}<br>Cured: ${cured}<br>Deaths:${deaths}'
                },
             iconCss: 'e-icons e-play-icon',
             cssClass: 'e-flat', isPrimary: true, content:'Print', style: 'text-transform:none !important'
          }
  },
provide: {
    maps: [ Legend, MapsTooltip]
},
methods:{
getMessage() {
      const path = 'https://still-gorge-33699.herokuapp.com/get-statecount';
      axios.get(path)
        .then((res) => {
          this.statecount = res.data;
//           for(let i = 0; i < this.statecount.length; i++){
//     this.statecount[i].name = this.statecount[i]['stateOrUnionTerritory'];
//     delete this.statecount[i].stateOrUnionTerritory;
// }
this.dataSource=this.statecount
console.log(this.dataSource)
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  
    tooltipRender:function(args){
         if (args.options.toString().indexOf('confirmedIndianNational') > -1) {
                args.cancel = true;
            }
    },
    clickToggle:function(args){
        this.$refs.maps.ej2Instances.print();
    }
},
 mounted() {
    this.getMessage();
 }
})
</script>

