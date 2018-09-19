<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Article extends Model
{
    
    protected $table = "newsitem";
    
    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
    	'title', 'content', 'url', 'thumbnail', 'site_name', 'archive_type', 'cat_id', 'slug'
    ];

    public function category() {
    	return null;
    	// return $this->belongsTo('App\Category');
    }
}
