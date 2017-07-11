-- Filename: DB_Equip.lua
-- Author: auto-created by yexiao`s ParseExcel(to lua) tool.
-- methods: X.getDataById(id), X.getArrDataByField(fieldName, fieldValue)
-- Function: no description.

local keys = {
	"id","itemType","itemName","itemInfo"
}

local data = {
[1]={1,1,"头盔","战士"},
[2]={2,2,"盔甲","剑客"},
[3]={3,nil,"手套",nil},
[4]={4,4,"背包","药师"},
}

cc.exports.DB_Equip = {}
function DB_Equip.getDataById(id)
    if not id or type(id) ~= 'number' then return nil end
    local tmp = data[id]
    if not tmp then return nil end
    local tbl = {}
    for k,v in pairs(keys) do
         tbl[v] = tmp[k]
     end
     return tbl
end