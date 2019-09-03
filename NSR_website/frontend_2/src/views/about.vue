<template>
  <div class="about_container">
    <mynavbar></mynavbar>
    <div class="the_main_title">
      <div class="title_position">
        <h1 class="company_name">About the Vibrancy Index</h1>
      </div>
    </div>
    <div class="concept">
      <div class="title">What is the Vibrancy Index?</div>
      <div class="mid">
        <p>The Vibrancy Index is a research and reporting tool developed by a team of university students hired by New Sun Rising (NSR), a Pittsburgh-based non-profit which strengthens under-resourced organizations and provides accessible funding to build vibrant communities.. The Index provides data that shows what culture, sustainability, opportunity, and overall vibrancy looks like in Allegheny County communities.</p>
        <p>This Index can be used by residents and leaders alike to locate data that identifies specific needs. This information can help them to be more competitive and successful in attracting resources for solutions that are inclusive of residents and their communities. Future versions will show how Vibrancy Index scores change over time and how nonprofit outcomes are impacting conditions throughout Allegheny County.</p>
        <p>Many factors impact the level of vibrancy in each community and how that influences equitable development investment priorities. When curating this interactive map, NSR chose to focus on 16 out of 17 United Nations Sustainable Development Goals (UN SDGs), ranging from no poverty to reduced inequalities. These goals hit upon topics of sustainability, health and wellness, and overall quality of life through education and equal access to opportunity. We believe that these goals can only be achieved through continuous and collaborative efforts of everyone participating in the community - residents, elected officials, business owners, and employees. Although quality of life and opportunity measures vary greatly from neighborhood to neighborhood, most socioeconomic indexes are not sensitive enough to identify these disparities at the census level. </p>
        <p>The multidimensional nature of the Index allows for a larger scope of community health beyond basic economic measures. The Vibrancy Index includes indicators within three categories of community vibrancy: Culture, Sustainability, Opportunity</p>
      </div>
    </div>
    <div class="split"></div>
    <div class="data_area">
      <div class="title">DATA AND SCORING</div>
      <div class="mid">
        <p>The Vibrancy Index is a composite measure that draws upon important economic, educational, health, and community-related indicators of vibrancy. The Index was launched in 2019 and provide insight into the multidimensional nature of vibrancy in Allegheny County. The indicators are broken down geographically based primarily on census tracts to measure vibrancy for individual boroughs and neighborhoods, as well as aid community influencers and other stakeholders as they work to accelerate equitable growth across the county.</p>
        <p>This analysis begins an examination of what disparities persist across communities and to help guide communities' investment priorities.</p>
        <p>Each category of the Index includes three to seven indicators -- the specific measurements used to quantify vibrancy.</p>
        <div style="margin-top: 20px; margin-bottom: 20px;">
          <mytable></mytable>
        </div>
      </div>
    </div>
    <div class="split"></div>
    <div class="method_area">
      <div class="title">Methodology</div>
      <span class="mid">The Vibrancy Index draws upon statistics from a variety of sources (list these sources like ESRI, Labor Bureau, specific crime departments).</span>
      <div style="height:20px; width:100%;"></div>
      <div class="mid">
        <h6>Our 1st Step</h6>
        <p>The diverse indicators that comprise the Vibrancy Index include percentages and scales typically between 1-10. To include them in a composite measure such as the Vibrancy Index, we transform each of these statistics to enable comparisons on a common scale.</p>
        <p>Each tract's performance on an indicator is compared with the highest and lowest scores obtained on that indicator, excluding outliers (extreme values).</p>
        <p>The indicators in the Vibrancy Index vary in their directionality. For example, median household income is an indicator for which higher values are more desirable, but the unemployment rate is better when lower.</p>
        <h6>Our 2st Step</h6>
        <p>At the census tract level, the Vibrancy Index is made up of (#?) indicators across the three categories (Culture, Opportunity, and Sustainability). Each indicator is normalize using Minmax approach. This means that the assigned value to given tract is relative to the tract with the highest score of the sample, where the maximum score is 100.</p>
        <p>In each category, the rescaled values for indicators are averaged to create category-level Vibrancy Scores, also ranging from 0 to 100. Because data for some indicators are not available at the county or tract level, each census tract Vibrancy Index is made up of 38 of indicators.</p>
        <h6>Our 3st Step</h6>
        <p>Each tract also has an overall Vibrancy Score that summarizes performance across the three Index categories. To calculate these, a state's three category scores are averaged with equal weighting. Final Vibrancy Scores are again represented as values from 0 to 100; these values are used to rank all of the census tracts across Allegheny County.</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.about_container{
  height: 100%;
  width: 100%;
}

.mid{
  margin-left:20%;
  width: 60%;
}

.the_main_title{
  height: 200px;
  width: 100%;
  background-color: #4694B5;
}

.title_position{
  position:absolute;
  left: 28%;
  width: 40%;
  margin-top: 70px;
  text-align: center;
}

.the_company_introduction{
  width: 100%;
  height: 300px;
}

.concept{
  width: 100%;
  height: 650px;
}

.title{
  font-family: 'Oswald', 'Helvetica Neue', Arial, Helvetica, sans-serif;
  font-size: 30px;
  text-align: center;
  margin-top: 20px;
  margin-bottom: 20px;
}

.data_area{
  width: 100%;
  height: 1000px;
}

.method_area{
  width: 100%;
  height: 600px;
}

.footer{
  width: 100%;
  background-color: #1C3854;
  height: 300px;
}

.split{
    margin-top: 50px;
    width: 80%;
    border: 0.5px solid;
    margin-left: 10%;
    margin-bottom: 50px;
}
</style>

<script>
import Mynavbar from '@/components/navbar.vue'
import Mytable from '@/components/table.vue'
export default {
  components: {
    Mynavbar,
    Mytable
  },
  data () {
    return {
      title: ''
    }
  }
}
</script>
