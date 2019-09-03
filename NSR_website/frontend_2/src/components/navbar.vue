<template>
  <nav class="mynavbar">
    <div class="nav_container">
      <ul class="header_menu">
        <li>
          <v-link href="/">HOME</v-link>
        </li>
        <li>
          <v-link href="/explore">EXPLORE</v-link>
        </li>
        <li>
          <v-link href="/about">ABOUT</v-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<style>
.mynavbar {
  border: none;
  background-color: white;
  position: relative;
  min-height: @navbar-height;
  margin-bottom: @navbar-margin-bottom;
  border: 1px solid transparent;

  // Prevent floats from breaking the navbar
  &:extend(.clearfix all);

  @media (min-width: @grid-float-breakpoint) {
    border-radius: @navbar-border-radius;
  }
}

ul {
  list-style-type:none;
  padding:0px;
  margin:0px;
}

ul li {
  float:left;
  margin-right: 40px;
}

.nav_container{
  height: 50px;
  background-color: white;
}

.header_menu{
  right: 10%;
  margin-top: 20px;
  margin-left: 60%;
  top: 50%;
}

.menu_herf{
  hieght:50px;
  font-family: 'Oswald', 'Helvetica Neue', Arial, Helvetica, sans-serif;
  font-size: 25px;
  color : #1C3854;
  border: none;
  background-color: white;
}

</style>

<script>
import VLink from '@/components/VLink.vue'

export default {
  components: {
    VLink
  }
}
</script>
