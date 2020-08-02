## OpenShift, изучение и структурирование информации


### Что такое OpenShift (что необходимо знать перед тем как начать работать с OpenShift)

#### Описание OpenShift    
__OpenShift__ – это семейство программного обеспечения для контейнеризации потоков данных, разработанное компанией Red Hat.    
Его флагманским продуктом является контейнерная платформа _OpenShift_ –локальная платформа-сервис,    
построенная вокруг контейнеров Docker, организованных и управляемых _Kubernetes_ на базе _Red Hat Enterprise Linux._    
Другие продукты семейства предоставляют эту платформу через различные среды:    
_OKD_ служит ориентированным на сообщество восходящим потоком (сродни Fedora);   
_OpenShift Online_ – предлагается в качестве сервисного программного обеспечения;   
_OpenShift Dedicated_ – это платформа, предлагаемая в качестве управляемого сервиса.   

#### Что следует уяснить сразу?
Как следует из определения, взятого из Википедии, «это семейство программного обеспечения для контейнеризации…»    
Чтобы порог входа в эту технологию не показался непосильным, нужна иметь представление о ПО, которые лежат в основе _OpenShift_,   
а именно, – о технологиях _Docker_ и _Kubernetes._

__Docker__ это контейнерная визуализация, позваляющая поставлять приложения вместе со средой для запуска, а именно:    
* Docker Image – готовый образ, выложенный на DockerHub.    
* Dockerfile – инструкция для создания контейнера на базе образа.    
* Docker Container – ваша виртуальная машина, изолированная от основной. OC, с вашим приложением и настройками.    

Не могу здесь остановится подробнее, так как не это есть цель статьи, зато подробней остановлюсь на _Kubernetes_.    
И вот почему:    
Во-первых, это объяснит необходимость знаний перечисленных технологий.    
Во-вторых, плавно введет в новую технологию _OpenShift_.    
И я надеюсь, это объяснит некоторую непоследовательность моего повествования, и то, почему мы начинаем "из далека".    

__Kubernetes__ или __k8s__, как я упомянул выше, – это средство автоматизации для контейнеризованных приложений для их развертывания, масштабирования и управления.    
Основной компонент __k8s__ – это _Cluster_    
Вы создаете _Kubernetes Cluster_, состоящий из _Nodes_ (узлов)    
_Nodes_ существует двух типов:     
* __Worker Node__ – сервер на котором запускаются и работают приложения.
  + __kube-apiserver__ – развертывание и управление жизненным циклом контейнеров.
  + __kube-controller-manager__ – отслеживает состояние и приводит кластер к желаемому виду
  + __kube-sheduler__ – выбирает узел, на котором должны работать поды
  + __etcd__ – основное хранилище всех данных кластера в Kubernetes.
    - __Pod__ – это докер-контейнер. Иногда их – несколько. Работают внутри Worker Node.
* __Master Node__ – сервер который управляет Worker Nodes.
  + __kubelet__ – получает команды от kube-apiserver
  + __kube-proxy__ – сетевой интерфейс каждого Node.


Для установки Kubernetes вам понадобится три вещи:    
* сервер или виртуальный сервер (многие облачные сервисы уже давно имеют этот функционал).
* _kubestl_ – программу для управления _Cluster_ (все команды посылаются на _Master Node_).
* программа для создания _Cluster_ (ее выбор зависит от конкретного используемого облачного сервиса).

И так, в основе всего Kubernetes лежат контейнеры докер и управления ими    
В то время как под капотом _OpenShif_ лежит 100% _Kubernetes_, c тем отличаем,    
что _OpenShif_ это функционал расширил, добавил удобные фишки.   
Только называется это уже по-другому: _OC_ (сокращение от _OpenShift client_).

Далее я просто хочу показать, как выглядят команды _Kubernetes_ и _OpenShift_

| Команды kubectl |	Команды OC | Значение |
|-----------------|------------|----------|
| kubectl get pods | oc get pods | возвращает поды |
| kubectl get namespaces | oc get namespaces | возвращает пространства имен |
| kubectl create -f deployment.yaml |	oc create deployment.yaml |	собирает из deployment.yaml |

Любой проект собранный на основе kubernetes будет работать и на OpenShift.    
Также, установив ОС, мы получаем дополнительный функционал, помимо расширенного набора команд в CLI.    

* Мониторинг контейнера с использованием Grafana.
* Это полноценная система _CI/CD_, работающая, в том числе, и на основе контейнеризованного графического интерфейса Jenkins.
* Виртуальные машины можно открывать прямо в OpenShift c использованием Container Native Virtualization.
* Улучшенный функционал _ODO_ (улучшенная версия kubectl для разработчиков).
* Система поддерживает языки: _Go, Node, JS, Ruby, Python, Java, Perl, PHP._
* _Codeready Workspaces_ – полностью контейнеризованная IDE с веб-интерфейсом.

__Подытожим__

_Red Hat OpenShift_ поддерживается _Kubernetes_ для облачных приложений с корпоративной безопасностью.    
_OpenShift_ часто называют _«Enterprise Kubernetes»._    
Оригинальная версия облегчает разработку и развертывание приложений в облаке    
и добавляет инструменты поверх ядра _Kubernetes_ для ускорения процесса разработки и развертывания.

Также хочу добавить, облачные сервисы, "большие" и "маленькие" давно взяли на вооружение передовую технологию _Kubernetes_ и имеют возможность внедрения надстройки _OpenShift_    

* Google Cloud Platform
* Amazon Web Services
* Microsoft Azure
* Nanobox
* OutSystems Platform
* Heroku

_Red Hat_ не раз лазил в исходники _Kubernetes_ и добавлял новый функционал в первоисточник,    
но при этом у _Red Hat_ готовый продукт, который можно брать на вооружение и решать бизнес задачи.    
_OpenShif_ следит за обновлениями всех доступных инструментов и слажености в их работе, обеспечивает безопасть и многое дугое, тем самым давая разработчикам и DevOps инженерам сконцентрироваться на решении задачи и избавить от лишней работы.


### Перенос инструментария НТ (нагрузочное тестирование) в OpenShift. Подготовительные работы и открытые вопросы. (Возможны узкие места при проведении НТ, что требует дополнительного изучения).

Чтобы не лезть в дебри, уходя от конкретного проекта, считаю логичным пробежаться по плану и попытаться предугадать,    
будет ли наше плавание рейсом судна, доставляющего контейнеры строго по расписанию,    
или – побывав между Сциллой (заказчиком) и Харибдой (временем, столь быстро утекающим, что водоворот создающим), – разобьет нашу трирему и выкинет на остров Огигия. (Навеяно морской тематикой Docker и Kubernetes)


#### 1. Анализ контейнеров, которые есть в open source.

DockerHub – огромный репозиторий без ограничений на выбрасывание чего угодно: будь то готовый продукт или просто личный тест для себя новой технологии под названием _Docker._    
С одной стороны, можно найти что угодно, а с другой, – в любом случае придется разбираться, что там под капотом и переделывать все это под свои нужды.    
Конечно, эта проблема вообще не встает при наличии официальных образов, которые для нас уже разработаны.

Если _kubernetes_ в любом другом облачном сервисе можно использовать под любой зоопарк семейства _Linux_, то строгость красной шляпы (_Red Hat_) состоит в том, что ее покровительство в обслуживании софта, обязует нас использовать _Red Hat Enterprise Linux_ на базе _Fedora._    
Контейнеры хоть и подразумевают изолированность от основной _ОС_, где они существуют, но чувствуется, еще предстоит проверить, так ли это с точки зрения потребляемых мощностей.    
А вдруг изолированный дистрибутив почувствует родственную душу в оболочке снаружи и будет работать лучше, а потреблять меньше… Или все это зависит от _ОС_ в изоляторе?


#### 2. Установка и разворачивание контейнера в OpenShif..

Проброс портов для мониторинга бизнес метрик в influx,
Просмотр встроенных инструментов мониторинга OpenShift.

Red Hat продукт корпоративного класса со всей строгостью слова "Enterprise" в названиях своих продуктов.
Это берет на себя ответственность в таких вещах как аутентификацию, сеть, безопасность, поддержка сопутствующих инструментов и все обновления и совместимость и целостность внутренней экосистемы.
Я немного переживал: ожидал увидеть скромный личный DockerHub от Red Hut с ожидаемым названием DockerHut, на тот момент я забыл об их политике открытого кода, и был в полной уверенности, что все собирать нужно будет через Dockerfile (Благо доступ к привычному DockerHub – не проблема).

Немного изучив документацию, я нашел, как открыть доступы и запустить тестовый apаche-server c привычным тестовым «Hello, world». И полюбоваться на него. Как из среды OpenShift Online, так и, набрав адрес на своей машине.

Еще предстоит внимательно изучить документацию на предмет получаемых доступов, но заголовки в документации: «подключение дисков извне», «доступ к консоли для каждого контейнера» и огромный раздел «Сеть» дают понимание о большом функционале и вселяют уверенность в выполнении задачи.


#### 3. Разработка/актуализация сценария jmeter под этот проект.

Убедимся, что не упираемся по производительности в инструментарий docker

Момент, который точно придется изучить – это наличие ограничений сетевой активности _nods_ (узлов) в самом _OpenShift_, так как это вызывает некоторые сомнения.
Это будет зависеть еще и от выбранного проекта; и от того, с какими протоколами работают скрипты. И есть ли внешние данные, которые используют скрипты; и нужно ли хранить результаты. И если да, то определиться с выбором.

Тут я полагаю, что только на практике, наблюдая за метриками потребляемыми контейнером, и анализируя, их мы сможем получить ответы «На какие рифы мы напоремся» или поплывем «по ветру быстрее ветра».


#### 4. Проведение серии нагрузочных тестов для сравнения подходов НТ (docker vs KHC).
Убедимся, что не упираемся по производительности в инструментарий Docker.

На данном этапе нам придется объединить все заготовки для OpenShift, развернуть и все отладить, попробовать различные варианты.
