<template>
  <div class="current-time">
    Current time:
    <p>{{ localTime() }}</p>
  </div>
</template>

<script>
export default {
  name: 'CurrentTime',
  props: {
    time: null,
  },
  methods: {
    localTime(){
      return new Date(this.time).toLocaleString();
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
