require "ArcherSysOS/version"



module ArcherSysOS

  
class WeakHash < Hash
  def []= key, obj
    super WeakRef.new(key), WeakRef.new(obj)
  end
end

end

