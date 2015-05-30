<?php
   namespace ArcherSys\Auth\OAuth2;
   require_once $_SERVER["DOCUMENT_ROOT"]."/vendor/autoload.php";
   use Auth0\SDK\Auth0;
    class ArcherAuth2{
       
     function __construct(){
      $this->auth0 = new Auth0(array(
    'domain'        => 'archersysos.auth0.com',
    'client_id'     => 'o6FbQv6OHn9o9PTiKsrvU1epTjtAFLIQ',
    'client_secret' => 'Zx2A1XXN3A_1W6rB23gs8usK0srZn2f6_s9R2tyu1TC3PF0qeKrOVs7BS_RSGzCx',
    'redirect_uri'  => 'http://localhost/Alonzo/OI'
));
    
}
     function go(callable $onAuthenticated){
      $this->auth0->getUser();
      if (!$userInfo) {
       ArcherAuth2::authenticate();
     } else {
       $onAuthenticated();
     }
}
  static function authenticate(){
  ?>
<script src="https://cdn.auth0.com/js/lock-7.1.min.js"></script>
<script type="text/javascript">
  
  var lock = new Auth0Lock('o6FbQv6OHn9o9PTiKsrvU1epTjtAFLIQ', 'archersysos.auth0.com');
  
  
  function signin() {
    lock.show({
        callbackURL: 'http://localhost/Alonzo/OI'
      , responseType: 'code'
      , authParams: {
        scope: 'openid profile'
      }
    });
  }
</script>
<button onclick="signin()">Login</button>
<?php
}
}
?>