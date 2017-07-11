# Excel2Lua
 将excel表导出cocos 能用的lua

### excel2csv
在终端中运行
	
	python excel2csv.py excel/role.xls csv/role.csv 0
可以将excel文件转换为csv 这个只是简单的转换，服务器可以根据csv转换为json或者xml形式

### excel2lua
终端运行
	  
	  python excel2lua.py excelDir luaDir
1.规范sheet 中|线分割前面为注释，后面为导出的lua文件名，形如角色|role  
2.excel中第一行为注释、第二行为类型（目前支持int、string、bool、table）、第三行为字段名字。其中第二行可以通过|分割是否只有前端或者后端导出，形如table|client  
3.默认第一列为id，并且为int不重复的自增类型，因为导出的lua表中要用这个来查找数据。
4.表中的数据可以为空，lua导出时候是为nil(bool类型为false)
### TODO
1.添加git支持
2.添加scp支持
3.多类型判断及对excel表做检查