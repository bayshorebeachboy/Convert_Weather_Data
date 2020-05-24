select `Temperature`, `Month`, `Day`, `Year`, `Hour`
from `Combined`
where `Temperature` = (select MAX(`Temperature`) from `Combined`)

